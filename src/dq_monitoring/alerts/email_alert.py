import smtplib
from email.message import EmailMessage

from config.db_config import DBConfig


def send_email_alert(results: list[dict], run_id: str) -> bool:
    failed_results = [result for result in results if result["status"] == "FAIL"]
    if not failed_results:
        print("Email alert skipped: no failed checks.")
        return False

    if not DBConfig.EMAIL_ALERT_ENABLED:
        print("Email alert skipped: EMAIL_ALERT_ENABLED=false")
        return False

    message = EmailMessage()
    message["Subject"] = f"Data Quality Alert - run_id {run_id}"
    message["From"] = DBConfig.EMAIL_SENDER
    message["To"] = DBConfig.EMAIL_RECIPIENT
    message.set_content(build_email_body(failed_results, run_id))

    with smtplib.SMTP(DBConfig.SMTP_HOST, DBConfig.SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(DBConfig.EMAIL_SENDER, DBConfig.EMAIL_PASSWORD)
        smtp.send_message(message)

    print("Email alert sent successfully.")
    return True


def build_email_body(failed_results: list[dict], run_id: str) -> str:
    lines = [f"Data quality issues detected for run_id={run_id}", ""]
    for result in failed_results:
        lines.append(
            f"- {result['check_name']} | {result['column_name']} | "
            f"issue_count={result['issue_count']}"
        )
    return "\n".join(lines)

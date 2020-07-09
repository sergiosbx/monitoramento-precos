import yagmail
from dataclasses import dataclass, field

from variables import MAIL_USERNAME, MAIL_PASSWORD, MAIL_SUBJECT, MAIL_TEMPLATE_HEADER, MAIL_TEMPLATE_BODY


@dataclass
class MailSender():
    receiver: str
    message: str = field(default="")

    def with_message(self, description, price, last_price, anchor):
        self.message = MAIL_TEMPLATE_HEADER + MAIL_TEMPLATE_BODY.format(
            description=description, price=price, last_price=last_price, anchor=anchor)

    def send(self):
        with yagmail.SMTP(user=MAIL_USERNAME, password=MAIL_PASSWORD) as smtp:
            smtp.send(to=self.receiver, subject=MAIL_SUBJECT, contents=self.message)

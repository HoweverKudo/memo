gmail_obj = MIMEText(inputs['body'])
        gmail_obj['to']  = inputs['to_address']
        gmail_obj['subject'] = inputs['subject']
        batch.add(account.google_gmail_client.users().messages().send(
            userId='me',
            body={
                'raw': base64.urlsafe_b64encode(
                    gmail_obj.as_bytes()
                ).decode()
            }
        ))
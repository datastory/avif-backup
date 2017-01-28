# Záloha dat z AVIF
Skript pro Amazon Lambda, který zálohuje uživatelská pozorování z [databáze AVIF](http://www.birds.cz/avif/) do S3.

Před nahráním nutno nainstalovat knihovnu **requests** příkazem  `pip install requests -t ./`, vyplnit přístupové údaje do AVIF v souboru `credentials.py`, následně pak obsah celé složky [zabalit do ZIP balíčku a nahrát do do Lambdy](http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html).

Lambda funkce musí mít nastavené [oprávnění pro zápis do S3](http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-create-iam-role.html) a také příslušný [trigger, který ji čas od času spustí](http://docs.aws.amazon.com/lambda/latest/dg/with-scheduled-events.html).

Більченятко аналізує нову атаку на безпечний месенджер, і знайшло помилку в обробнику контент провайдера. У логах телефону багато помилок, але нащастя немає виводу імен і паролів -- все добре. Знайдено джерело помилок, їх можна отримати за допомогою команди

```adb shell content query --uri content://com.secure.messenger/users --projection name:value --where "name=1 select sql from sqlite_master where substr(hex(sql),1,1)='4'"```

Лог з досліджуваної системи у додатку. Допоможіть більченяткові дописати звіт і піти додому раніше.
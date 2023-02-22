**Example 1: 户口本识别示例代码**

居民户口簿户主页及成员页关键字段的识别，包括姓名、户别、地址、籍贯、身份证号码等

Input: 

```
tccli ocr ResidenceBookletOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg
```

Output: 
```
{
    "Response": {
        "Address": "",
        "BirthDate": "1999年09月19日",
        "BirthPlace": "上海市",
        "BloodType": "",
        "EducationDegree": "小学",
        "FormerName": "李新星",
        "Height": "",
        "HomePageNumber": "",
        "Household": "",
        "HouseholdNumber": "",
        "HouseholderName": "",
        "IdCardNumber": "310110199909192329",
        "IssueDate": "",
        "MaritalStatus": "未婚",
        "MoveToCityInformation": "",
        "MoveToSiteInformation": "",
        "Name": "李晨曦",
        "Nation": "汉",
        "NativePlace": "江苏省江阴市",
        "OtherAddresses": "",
        "Profession": "",
        "RegistrationDate": "2010年07月13日",
        "Relationship": "子",
        "ReligiousBelief": "",
        "RequestId": "037d6b99-6ca4-401a-a537-fe5e16f1d777",
        "ServicePlace": "丰镇小学",
        "Sex": "男",
        "Signature": "",
        "VeteranStatus": ""
    }
}
```


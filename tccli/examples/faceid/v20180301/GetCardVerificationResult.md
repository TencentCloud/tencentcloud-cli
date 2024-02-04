**Example 1: 正常响应**



Input: 

```
tccli faceid GetCardVerificationResult --cli-unfold-argument  \
    --CardVerificationToken abc
```

Output: 
```
{
    "Response": {
        "Status": "abc",
        "WarnInfo": [
            "abc"
        ],
        "Nationality": "abc",
        "CardType": "abc",
        "CardSubType": "abc",
        "CardInfo": {
            "HKIDCard": {
                "CnName": "abc",
                "EnName": "abc",
                "TelexCode": "abc",
                "Sex": "abc",
                "Birthday": "abc",
                "Permanent": "abc",
                "IdNum": "abc",
                "Symbol": "abc",
                "FirstIssueDate": "abc",
                "CurrentIssueDate": "abc"
            },
            "MLIDCard": {
                "Name": "abc",
                "ID": "abc",
                "Sex": "abc",
                "Address": "abc",
                "Type": "abc",
                "Birthday": "abc"
            },
            "PhilippinesVoteID": {
                "VIN": "abc",
                "FirstName": "abc",
                "LastName": "abc",
                "Birthday": "abc",
                "CivilStatus": "abc",
                "Citizenship": "abc",
                "Address": "abc",
                "PrecinctNo": "abc"
            },
            "IndonesiaIDCard": {
                "NIK": "abc",
                "Nama": "abc",
                "TempatTglLahir": "abc",
                "JenisKelamin": "abc",
                "GolDarah": "abc",
                "Alamat": "abc",
                "RTRW": "abc",
                "KelDesa": "abc",
                "Kecamatan": "abc",
                "Agama": "abc",
                "StatusPerkawinan": "abc",
                "Perkerjaan": "abc",
                "KewargaNegaraan": "abc",
                "BerlakuHingga": "abc",
                "IssuedDate": "abc",
                "Provinsi": "abc",
                "Kota": "abc"
            },
            "PhilippinesDrivingLicense": {
                "Name": "abc",
                "LastName": "abc",
                "FirstName": "abc",
                "MiddleName": "abc",
                "Nationality": "abc",
                "Sex": "abc",
                "Address": "abc",
                "LicenseNo": "abc",
                "ExpiresDate": "abc",
                "AgencyCode": "abc",
                "Birthday": "abc"
            },
            "PhilippinesTinID": {
                "LicenseNumber": "abc",
                "FullName": "abc",
                "Address": "abc",
                "Birthday": "abc",
                "IssueDate": "abc"
            },
            "PhilippinesSSSID": {
                "LicenseNumber": "abc",
                "FullName": "abc",
                "Birthday": "abc"
            },
            "PhilippinesUMID": {
                "Surname": "abc",
                "MiddleName": "abc",
                "GivenName": "abc",
                "Sex": "abc",
                "Birthday": "abc",
                "Address": "abc",
                "CRN": "abc"
            },
            "InternationalIDPassport": {
                "LicenseNumber": "abc",
                "FullName": "abc",
                "Surname": "abc",
                "GivenName": "abc",
                "Birthday": "abc",
                "Sex": "abc",
                "DateOfExpiration": "abc",
                "IssuingCountry": "abc",
                "NationalityCode": "abc",
                "PassportCodeFirst": "abc",
                "PassportCodeSecond": "abc"
            },
            "GeneralCard": {
                "LicenseNumber": "abc",
                "PersonalNumber": "abc",
                "PassportCodeFirst": "abc",
                "PassportCodeSecond": "abc",
                "ExpirationDate": "abc",
                "DueDate": "abc",
                "IssuedDate": "abc",
                "IssuedAuthority": "abc",
                "IssuedCountry": "abc",
                "FullName": "abc",
                "FirstName": "abc",
                "LastName": "abc",
                "Sex": "abc",
                "Age": "abc",
                "Birthday": "abc",
                "BirthPlace": "abc",
                "Nationality": "abc",
                "RegistrationNumber": "abc",
                "Address": {
                    "Country": "abc",
                    "PostalCode": "abc",
                    "Subdivision": "abc",
                    "City": "abc",
                    "FormattedAddress": "abc",
                    "LineOne": "abc",
                    "LineTwo": "abc",
                    "LineThree": "abc",
                    "LineFour": "abc",
                    "LineFive": "abc"
                }
            },
            "IndonesiaDrivingLicense": {
                "LastName": "abc",
                "FirstName": "abc",
                "LicenseNumber": "abc",
                "Birthday": "abc",
                "Address": "abc",
                "ExpirationDate": "abc",
                "IssuedDate": "abc",
                "IssuedCountry": "abc"
            },
            "ThailandIDCard": {
                "LastName": "abc",
                "FirstName": "abc",
                "LicenseNumber": "abc",
                "DateOfBirth": "abc",
                "DateOfExpiry": "abc",
                "DateOfIssue": "abc",
                "IssuedCountry": "abc"
            },
            "SingaporeIDCard": {
                "ChName": "abc",
                "EnName": "abc",
                "ID": "abc",
                "Sex": "abc",
                "CountryOfBirth": "abc",
                "Birthday": "abc",
                "Address": "abc",
                "Race": "abc",
                "NRICCode": "abc",
                "PostCode": "abc",
                "DateOfExpiration": "abc",
                "DateOfIssue": "abc"
            }
        },
        "IDVerificationToken": "abc",
        "RequestId": "abc"
    }
}
```


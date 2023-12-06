**Example 1: 获取Web核验服务结果信息**



Input: 

```
tccli faceid GetWebVerificationResultIntl --cli-unfold-argument  \
    --BizToken EE13636D-1985-42CA-BD61-73F4C8B687E6
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "ErrorMsg": "abc",
        "VerificationDetailList": [
            {
                "ErrorCode": 0,
                "ErrorMsg": "abc",
                "LivenessErrorCode": 0,
                "LivenessErrorMsg": "abc",
                "CompareErrorCode": 0,
                "CompareErrorMsg": "abc",
                "ReqTimestamp": 1,
                "Similarity": 0,
                "Seq": "abc"
            }
        ],
        "VideoBase64": "abc",
        "BestFrameBase64": "abc",
        "OCRResult": [
            {
                "IsPass": true,
                "CardImageBase64": "abc",
                "CardInfo": {
                    "HKIDCard": {
                        "CnName": "abc",
                        "EnName": "abc",
                        "IdNum": "abc",
                        "Birthday": "abc",
                        "Sex": "abc"
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
                    }
                },
                "RequestId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```


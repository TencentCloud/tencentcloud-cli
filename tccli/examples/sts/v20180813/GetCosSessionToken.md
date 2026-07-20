**Example 1: 下发只读临时密钥三元组**



Input: 

```
tccli sts GetCosSessionToken --cli-unfold-argument  \
    --SessionMode ReadOnly \
    --Resource qcs:id/0:cosrapid:ap-chengdu:uid/251433186:prefix//123456/my-bucket/ \
    --UserAuthToken 9ou6TjEH6inmLIUiTwZRrf6uFOhn74oof5ea1d523972c720ae084377b0c19868K6vZmyvx78xqT-nWKtlaGk9M1rw6M1THgiYczyQqhOGk4zxSYwOKpRuhp0Sju9alPkFoCQurBVF5MKp810OlyJyosRpZENJK2TcKYu8CF7G4gcwIaqnxF1o9OGqvPLVVurX6swUfFrmQ6tmGbsvswg \
    --UserUin 700002713397 \
    --UserOwnerUin 700002713397
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "TmpSecretId": "SKID_NGCa1nJi-XV1R-ZYzkrkPIQ6zft5LOhSMj3C50XCWgatTNkk6VNQfWShqzwWdTV",
            "TmpSecretKey": "0Gg++0mdKYi3/yeoTLVG4hcIG4cnV/RbLZioznnKFnc=",
            "Token": "CDFjbveQ43VhQlSABTnoMqgKU5FKHI2ad25f477132df9a5ab548cd7df6ef1382cabdaf470150154cccc3fd4ff0c529f5wYpZ-fUwUtmVz1LoDwu_-FHoJfLi6iCF6efXtGhgWx_-xMhS3Ew9zyYSFRIy9zZJzplsNRqD2_DMOjNqRgkyAEv1sVr4XDfVejmaYKyaNImXrui9LkZafJUs9gNlUHe8WjbtT-K-vaVKw8Yv0IYZw50HQdm4S3vS3ifdNY37xh1IEbhSFWGBRFtSrH52YZoXYadtk6fBDjhYtnTW_eiwOQot5OMjHJAouJOqZo6cmcFbTk8y1iU6afC7eD981ai5UV1bBUtpkYHvlm8hnhRs5Q"
        },
        "Expiration": "2026-07-15T13:01:30Z",
        "ExpiredTime": 1784120490,
        "RequestId": "2bbe0b19-4ab5-4a2d-a166-5071ac8ce2a8"
    }
}
```


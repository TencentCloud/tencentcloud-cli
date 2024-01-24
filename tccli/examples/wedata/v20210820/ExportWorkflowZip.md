**Example 1: 示例1**

导出工作流

Input: 

```
tccli wedata ExportWorkflowZip --cli-unfold-argument  \
    --ProjectId 1460726726769418240 \
    --WorkflowIds 25287aef-7226-11ed-8346-e43d1ad5f5f0 7bf9d403-7fb5-11ed-8346-e43d1ad5f5f0
```

Output: 
```
{
    "Response": {
        "Data": {
            "BucketName": "wedata-fusion-dev-1257305158",
            "BucketRegion": "ap-nanjing",
            "FileExpireTime": 1688807018,
            "FileMappings": [
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/export/1460726726769418240/1460726726769418240_workflows_20230623170338092.zip",
                    "OriginFileName": "1460726726769418240_workflows_20230623170338092.zip",
                    "TargetFileName": "1460726726769418240_workflows_20230623170338092.zip"
                }
            ],
            "SecretId": "AKIDm8idO32-h8JB0VORmr-U4iJvWu91_zDkDPgwv2kGOMb9D6rbm0ck3KuJCDU8EqcC",
            "SecretKey": "SIcPS0FKz9oXOXY2gPiLvfFjhJjFVpDo+2vctiT3soI=",
            "ShareStorageEndPoint": "service.cos.myqcloud.com",
            "ShareStorageType": "COS",
            "Token": "35A7Jdz9uwbijSzVBYYZKcgpOFn1yBDad4a26ba4dc36c23ffcb436b79fd48e01G_cfFo-D8aDzgnLMh2krQNeHbxeDNgUoaqlEAyrofYT63cxSB2W5GDk9H9wir68aBluiN-QvQkjSxTl0zzMPk19DcopBoxAAotP11mQVeeuf23RPrNg7-s1ohKqMDCMjUCjc2BoNXh3uTYtcpJST-0nn934OVujws1gzzLTh5lfqbMZlhjRdDEaHZcLdBsZUIphwhnTZIM94AODVWLC5nkpZ8vA--Zm6HKyaGJvoHMXgHW8CNdKwUHBEs-YxiieeHFCfH3Yz4iq0_zXB7tbaRHwRmPukLXAwqVgiw5uSDMNdi1Babuyj4djcyxLA2DEWR-9cOl4rIVq7NN0Eb9K-66ADxXOiU8a_FGWc6yMadkCzV3tVstQU17OPdIczjXU_aL6w2ZYWdlK6Bbc_8HvEr6M8pfKbEjtKSn7PGCiVINj5bJwvnLpn2kqU5W1Id14hQrZXa4W0Op-p5dW1k4XoBwDQvBCCSk08wJBn1Rt-Znb1a74lU21KTtB9OqqLcAXqOYsADSZGRhMnBdjAXheDu9pnx44cIfR-L9JtVj0FsbOPNDVpcSJ0hRkjNWk6fVo1mQ5LHUos4yD_WBiCqS_n1PHTfHbIcru2Arg3gXFGeHfEqTfJ9Jiqjf2qMTXuvpEzk7Q_H-UEi26xbSTfGUFA6v-ytV3F3FC5SyGsXCi-WIBWO7kTJ8wXJ6oeeGWOCgRjjHAKj6lItKJLvELAFGhSeosV_uOQerbZGp5igPGnwfO1r41Uz9CE-Z0BfOxQyxmJgu_npn9Hkm5e_mqy-MeGMBXbQLLtqOJAcDsxWkyZOK54pxVNck-0DkOaXDK3RaVmp2icPB52k2BqdokDu2lgbQ",
            "TokenCreateTime": 1687511018,
            "TokenExpiredTime": 1687518218
        },
        "RequestId": "679ac0d4-9587-42be-895b-de933aa775e7"
    }
}
```


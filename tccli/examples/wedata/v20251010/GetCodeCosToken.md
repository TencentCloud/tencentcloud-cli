**Example 1: IDE获取COS Token**

IDE获取COS Token

Input: 

```
tccli wedata GetCodeCosToken --cli-unfold-argument  \
    --WorkspaceId 1470547050521227264 \
    --RemotePath /ude/internal-hosting/oneflow/251436191/1470547050521227264/file-versions/f3d566ed-c898-48ab-a129-35da9f7d5ae3/data_0305.txt
```

Output: 
```
{
    "Response": {
        "Data": {
            "Bucket": "bucket-30-251436191",
            "Region": "ap-guangzhou",
            "Token": {
                "CreateTime": "1763373116",
                "CreateUserUin": "",
                "ExpiredTime": "1763380316",
                "OwnerUin": "700002164618",
                "SecretId": "AKIDFjefaR2qTpc4D1gcKtGMmrCNQ7jpwxbdtHOKGhEyoGu_PWQYBMXRiJdeJVf8diz3",
                "SecretKey": "c1HmT6TMKttLvc9tQVOpGZXqDgHfa2KPv/KtJNR/9Dw=",
                "Token": "OoTCKSwceENlY4p3eqWhnvl3C2KkEHjMeebe8902fc69c799fd7b078c75a1a63e1ll0jYSPxKROS5Ulai1RuuKsdT_Ehgb24B7Ebm4BAnr9NW5iu4L8APLK85AN4Cilkhm3Vqo7Rn2BaQ6Bst0xi_uCXsDto1Zd7rO4uTAnEetyXZit8FNjEr7S7fFdnRnoSl1BwzMDYC3QShWjWdlUD38Kfhj7F-q1Z6-UFvAFnbA04Kf6Nu1TD11ChPH9eH-0bRy2aHtxGLJ1eKMAySB0tAgaqkV6M7TldhKxKu8777OYr2qATrFntOkgpbjm3cIU0oNufVRML0d6OYi4ImR6k6Gys2pLWEHeg8ETaojRX1aOS5kM5bKYu7HZNlj0Hn9dSAk6IyGjpBg6Aba-JFlYEylzANiNOm6ZhKuRsx1xHeHzAJ0T28EDrhMIKmvspwQz-He1r1drA2ex6VnrdQW8Ppz-J4xdPqk0UySeToE_XvzWeeKaC_01K7zjG0Goi6HEkanh8E-KCYyDvHdwD-qpDFwOHYg-kHjbTpiq4G6FBNdRVfDuTeXkUNG3zUWT1nBPSgyCQb_EkYB_Bfd59g6WxrDv2AmargWKfDRuU9Zn4h_ychvVsaC_IBViwqX-u0z4wp8FuzDzqvKF5VmVZqW6aQzRec_RW7c-0L5VffOr7zSUzVawVMPbSjAWIhQsth2E6pfxTyNss3BlQRAdyw6v_HCql1qISDXvng0uqZwP5GI5knPz1aDDVS48WLb0A_pCttgS_anb7XdWWXRnMn7p6e2WCFPh2ArEkpOq-EO5tloxpYjUvw9gnKkcQNKDUt5Jugjr37ldQssIEEHPrWRCWSeVatQpZniaOfT_t4vXA0DFB7hw1an-777ehgo_3ghO_M19Vbz0K7Pvg1bFT0v0b_M6sbr_imfxuik7NGOVpc_UPfDTfGKS5mveBiSkj9hP4pKy2bBFPmfK5WmvYB_qlvqIs1EcI9fiDmXeN8rjjttzWKE-YLBSVUdivrEjEKeZGrB0SXDA2YHyRvBmeP9kVI7kOlg-Jt0oG9pXpO8i0MbQUGWvD__CnqoJXNdtaRz-IzruhUDVEYPsEHtA1guSkUgSJzZEIhh2q005o35J6sduHBjp0XFpiYL7q7OLVdCJqYHy2caoOa483r9KBCl76N5ldcC7cCNx2kogBa6k3IT-hEOeBj2F29iEE5Fl94J1YfnT2eiMxCeFKSfF_T5HxwCFg9Xd8y4jJuBjiQ5gXF9okaXmxAVRQCMu-PUDDFEevZ4vOb-du7pRlCuH3WfocCCLutcqbMxPPaO84ROTz39BC8J5fwqqh8E3YDFzgzGA6yQdrqzQ8Ff8ksjcvTRYDHXn8q_r6zRkKHuhQa8l6EVsN5J9dED0vlH4uVdo0YtUQkg4bPtLzC8no9fZF8eInTSNRzP7xktrVIQpmopJ-RfBhAvgvVNvUlbG45SdK_aaan0Sxy43pxDkug2QynZWMdlNZEsewr3HRjZ3pckQHh6OBatJzV7bKWihakcFDSO5iCX-sFLtVsWBs7YZE2gSs1ImZbIXw7NF87ZL_lBWea0F-V6fYs15Tw7NZfv708eBJYkU5o83kixAQP1yrxyrlpTVH_CN8dm_iP-1wkf9wYkkYzOzHZOxG2HzAcl-K6iae1-MOuIqW1fdXy0r3RwsMXZBkpY7K03jzf3PXfYzOs2-umsFW0fQNPogvnXBOz3Z4gtzbhGRS47cnGZn7zUpUDuX57YIdHVzI-cajVZ3K7XtvqX4Bf9gBr7ld9RPF8n5AP47mX2LemKWxgZB3cRUOO66h7Qc6mPvQqczvdA07CrSQEkuPAhSzqtjBzQjxr3ACfkgyvayp43_UpzFpIceuBc8wtVtznbryScqxtebwq623SD6ieJuSJraIYglkZtDlrhhLGYCJjdg4uR5tmBWCA"
            }
        },
        "RequestId": "9d23f026-b1c3-47f2-bdb0-309ff8eef964"
    }
}
```


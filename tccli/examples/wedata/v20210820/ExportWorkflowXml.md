**Example 1: 示例1**

导出工作流

Input: 

```
tccli wedata ExportWorkflowXml --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowIds ff7ac183-ed6c-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": {
            "BucketName": "wedata-fusion-dev-1257305158",
            "BucketRegion": "ap-nanjing",
            "FileExpireTime": 1688808063,
            "FileMappings": [
                {
                    "AbsoluteTargetFilePath": "/datastudio/tmp/export/1460947878944567296/workflow_2375850756392.xml",
                    "OriginFileName": "workflow_2375850756392.xml",
                    "TargetFileName": "workflow_2375850756392.xml"
                }
            ],
            "SecretId": "AKIDVxC7AFWjX17Ihf660uy91Qdwb8a38aM851KqbWXfp-NJ0wjr_T2LNyGwUD8ftfIl",
            "SecretKey": "YkhK8d2kOA3GBBGsI5RnyJtQpMnUbU4NHinNJm/VJLc=",
            "ShareStorageEndPoint": "service.cos.myqcloud.com",
            "ShareStorageType": "COS",
            "Token": "35A7Jdz9uwbijSzVBYYZKcgpOFn1yBDa017bf9dbf13584f8ac571af8e67a8917G_cfFo-D8aDzgnLMh2krQFhdqCNZixusmv7jEhV6HjM0UzAYoVOyF_wLHgC_8QHFWOYn9DAU8-fXzF4mKy_4Gg5WmFjSBJEAWp5zwhfpH7D9o8mpGK1fmWwUGbGpia6LXPPw1rLRlOTpOU9iIq4NBaZ5kGJS0CkZV-3j94FmZNcHh0vPac6d37ZN6JMttsUk_OLiVWPdXqYa68e6a7flnh9SrEyH-cyeit5q9ZuhqJMEI_nHeS69o-mJRl6N2FJrBjujwyUHgAbss5YgQOh-c8BOK9H0IYoLQUkTTGxW9urFlv7yZ-2O6wz_RCcu6iC1kbS_QbWH7974PL3ASzUxatu0i-LaDGzZz8iHR3x7ScwL-xv2AlJM7IRhnSNOLWmRoMIqy0McgcGf5azVB9HdLPpDjFfymBnQa0IUuayll2yNL8IOX7S1s5guFYu5qO0Ehs-zc2hCfyU-iQqaSDdDVdnFZ4sHOlUJzACR6NqT2UUHzOthJlK-2u2NNq44EbBnujcyyNyC_zqybS0UAhpd7ShMemhT4OUsla6f-tbsOJQ_YcedYn5mg06nlNXwNyZPKXFsdTvtc0EO1yHo6FxNgGb91Klm1IBNlf-KI33Z3CadDobHpDdolME9etkVmQlngJKidaCeV2gczwI8k4tFyrqBfo4P80JF1anlsZxgx_bwV-2XsMMETGceM9c9BoVkavmA3uz-pP8Y0WV_ia7YWEmM_1CSpQF1MdgNlb4lhCs9nhfEPf5yZ-IVRuochwf1AeyZIFwgDQXkDUojkqcCeZotrW_kiswSJRViNUVAF3g",
            "TokenCreateTime": 1687512064,
            "TokenExpiredTime": 1687519264
        },
        "RequestId": "a876c241-d3c4-4bd3-85e3-eeeab6ed5af2"
    }
}
```


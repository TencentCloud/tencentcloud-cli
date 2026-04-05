**Example 1: 查询IDE访问历史**

查询IDE访问历史

Input: 

```
tccli wedata ListCodeBrowsingHistories --cli-unfold-argument  \
    --WorkspaceId 1470547050521227264 \
    --PageSize 10 \
    --ResourceTypes IDE
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeBrowsingHistories": [
                {
                    "CreateTime": "1762245937961",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTMxLTI0LmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTMxLTI0LmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTMxLTI0LmlweW5iIn0=",
                    "ResourceId": "c9c3c93d-815f-403e-ae1d-d66ee67ce575",
                    "ResourceName": "2025-11-04_16-31-24.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762754906394"
                },
                {
                    "CreateTime": "1762245926511",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTQ1LTEwLmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTQ1LTEwLmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTQ1LTEwLmlweW5iIn0=",
                    "ResourceId": "4ac9c7c5-7deb-4698-a495-7eace7c1adc8",
                    "ResourceName": "2025-11-04_16-45-10.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762754888364"
                },
                {
                    "CreateTime": "1762249401139",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE3LTE0LTIyLmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE3LTE0LTIyLmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE3LTE0LTIyLmlweW5iIn0=",
                    "ResourceId": "87037509-9e39-4dce-ad1a-00779c83ade6",
                    "ResourceName": "2025-11-04_17-14-22.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762513351688"
                },
                {
                    "CreateTime": "1762255637644",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTUwLTI0LmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTUwLTI0LmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTUwLTI0LmlweW5iIn0=",
                    "ResourceId": "5240af1e-7712-4f16-912d-aab30cc49a55",
                    "ResourceName": "2025-11-04_16-50-24.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762513320451"
                },
                {
                    "CreateTime": "1762249443988",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvY2FuZG91d2FuZ190ZXN0LmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvY2FuZG91d2FuZ190ZXN0LmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvY2FuZG91d2FuZ190ZXN0LmlweW5iIn0=",
                    "ResourceId": "5de1f1a3-33a9-42dc-87d5-a64274ab5af5",
                    "ResourceName": "candouwang_test.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762497357826"
                },
                {
                    "CreateTime": "1762241856117",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvbGVvMTExLmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvbGVvMTExLmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvbGVvMTExLmlweW5iIn0=",
                    "ResourceId": "dcab42ae-c2a2-4445-aaee-b2fae79b69f1",
                    "ResourceName": "leo111.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762443809229"
                },
                {
                    "CreateTime": "1762246004503",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvbGVvZnR6aGFuZzEuaXB5bmIiLCJDRlNBYnNvbHV0ZVBhdGgiOiIvZGF0YS93ZWRhdGEvc2hhcmUvMTQ3MDU0NzA1MDUyMTIyNzI2NC9sZW9mdHpoYW5nMS5pcHluYiIsIkZpbGVBYnNvbHV0ZVBhdGgiOiIvV29ya3NwYWNlL2xlb2Z0emhhbmcxLmlweW5iIn0=",
                    "ResourceId": "e290c2d6-6d73-4429-ade6-39546939a4f4",
                    "ResourceName": "leoftzhang1.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762438505007"
                },
                {
                    "CreateTime": "1762244895254",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTExLTAwLmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTExLTAwLmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzE2LTExLTAwLmlweW5iIn0=",
                    "ResourceId": "235082e6-36f7-4af2-b548-36b4b467a20d",
                    "ResourceName": "2025-11-04_16-11-00.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762262562349"
                },
                {
                    "CreateTime": "1762170707757",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvbGVvZnR6aGFuZy5pcHluYiIsIkNGU0Fic29sdXRlUGF0aCI6Ii9kYXRhL3dlZGF0YS9zaGFyZS8xNDcwNTQ3MDUwNTIxMjI3MjY0L2xlb2Z0emhhbmcuaXB5bmIiLCJGaWxlQWJzb2x1dGVQYXRoIjoiL1dvcmtzcGFjZS9sZW9mdHpoYW5nLmlweW5iIn0=",
                    "ResourceId": "2a61d943-87cf-4997-b1cd-cb67cbc02c3c",
                    "ResourceName": "leoftzhang.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762238567438"
                },
                {
                    "CreateTime": "1762237349670",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzEyLTAxLTEyLmlweW5iIiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzEyLTAxLTEyLmlweW5iIiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvLmFzc2lzdGFudERpYWxvZy8yMDI1LTExLTA0XzEyLTAxLTEyLmlweW5iIn0=",
                    "ResourceId": "707ea531-27be-444b-821c-aaf5db7343e6",
                    "ResourceName": "2025-11-04_12-01-12.ipynb",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762237672620"
                },
                {
                    "CreateTime": "1762178027629",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvdGVzdDExMDEtMDEudHh0IiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvdGVzdDExMDEtMDEudHh0IiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvdGVzdDExMDEtMDEudHh0In0=",
                    "ResourceId": "8b00b9bf-844c-4ba5-bea8-223209f613fb",
                    "ResourceName": "test1101-01.txt",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762181657440"
                },
                {
                    "CreateTime": "1762178453326",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvdGVzdDExMDMtMDIudHh0IiwiQ0ZTQWJzb2x1dGVQYXRoIjoiL2RhdGEvd2VkYXRhL3NoYXJlLzE0NzA1NDcwNTA1MjEyMjcyNjQvdGVzdDExMDMtMDIudHh0IiwiRmlsZUFic29sdXRlUGF0aCI6Ii9Xb3Jrc3BhY2UvdGVzdDExMDMtMDIudHh0In0=",
                    "ResourceId": "0dae7799-0358-401b-8030-1553e4c3737d",
                    "ResourceName": "test1103-02.txt",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762178463536"
                },
                {
                    "CreateTime": "1762155755054",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvbGVvMTEwMy0xLnR4dCIsIkNGU0Fic29sdXRlUGF0aCI6Ii9kYXRhL3dlZGF0YS9zaGFyZS8xNDcwNTQ3MDUwNTIxMjI3MjY0L2xlbzExMDMtMS50eHQiLCJGaWxlQWJzb2x1dGVQYXRoIjoiL1dvcmtzcGFjZS9sZW8xMTAzLTEudHh0In0=",
                    "ResourceId": "8f0c850d-a311-449b-af04-5a63d2668125",
                    "ResourceName": "leo1103-1.txt",
                    "ResourceType": "IDE",
                    "UpdateTime": "1762163245672"
                },
                {
                    "CreateTime": "1761996347000",
                    "CreateUserUin": "700002164618",
                    "ExtraInfo": "eyJEaXNwbGF5UGF0aCI6Ii9Xb3Jrc3BhY2UvdGVzdDExMDEtMi50eHQiLCJDRlNBYnNvbHV0ZVBhdGgiOiIvZGF0YS93ZWRhdGEvc2hhcmUvMTQ3MDU0NzA1MDUyMTIyNzI2NC90ZXN0MTEwMS0yLnR4dCIsIkZpbGVBYnNvbHV0ZVBhdGgiOiIvV29ya3NwYWNlL3Rlc3QxMTAxLTIudHh0In0=",
                    "ResourceId": "222222-ed79-4432-8c79-e8e6ed623861",
                    "ResourceName": "test1101-2.txt",
                    "ResourceType": "IDE",
                    "UpdateTime": "1761996347000"
                }
            ]
        },
        "RequestId": "46a4c3a1-0571-4389-b829-76b42455f904"
    }
}
```


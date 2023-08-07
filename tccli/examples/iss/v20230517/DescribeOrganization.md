**Example 1: 成功1**

组织为空

Input: 

```
tccli iss DescribeOrganization --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "c67255e8-d4af-48e4-b6e1-c1aef3619be4"
    }
}
```

**Example 2: 成功2**

 

Input: 

```
tccli iss DescribeOrganization --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 1300000000,
                "OrganizationId": "111111",
                "Level": 1,
                "Name": "云api3",
                "Online": 0,
                "ParentId": "0",
                "ParentIds": "0",
                "Total": 0
            },
            {
                "AppId": 1300000000,
                "OrganizationId": "111112",
                "Level": 1,
                "Name": "云api3-2",
                "Online": 0,
                "ParentId": "0",
                "ParentIds": "0",
                "Total": 0
            },
            {
                "AppId": 1300000000,
                "OrganizationId": "111113",
                "Level": 1,
                "Name": "云api3-3",
                "Online": 0,
                "ParentId": "0",
                "ParentIds": "0",
                "Total": 0
            },
            {
                "AppId": 1300000000,
                "OrganizationId": "111114",
                "Level": 1,
                "Name": "云api3-4",
                "Online": 0,
                "ParentId": "0",
                "ParentIds": "0",
                "Total": 0
            },
            {
                "AppId": 1300000000,
                "OrganizationId": "111115",
                "Level": 1,
                "Name": "云api3-5",
                "Online": 0,
                "ParentId": "0",
                "ParentIds": "0",
                "Total": 0
            }
        ],
        "RequestId": "6e532d8b-883b-4c08-8f16-e46a33bc3944"
    }
}
```


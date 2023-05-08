**Example 1: 范例**



Input: 

```
tccli wedata DescribeFolderList --cli-unfold-argument  \
    --KeyWords  \
    --ProjectId 1 \
    --ParentsFolderId  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "476f49f3-8b40-46df-945c-89ca45246d77",
        "Data": {
            "TotalCount": 63,
            "PageNumber": 1,
            "PageSize": 10,
            "Items": [
                {
                    "Id": "b945f8ea-f135-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-06-21 15:42:38",
                    "Name": "111",
                    "ProjectId": "1",
                    "UpdateTime": "2022-06-21 15:42:38"
                },
                {
                    "Id": "bba029d7-fba0-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-07-04 21:53:50",
                    "Name": "aaa",
                    "ProjectId": "1",
                    "UpdateTime": "2022-07-04 21:53:50"
                },
                {
                    "Id": "1273e7fa-bfbd-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-04-19 16:45:32",
                    "Name": "aatest",
                    "ProjectId": "1",
                    "UpdateTime": "2022-04-19 16:45:32"
                },
                {
                    "Id": "0145078a-9e0e-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-03-07 19:59:12",
                    "Name": "abel",
                    "ProjectId": "1",
                    "UpdateTime": "2022-03-07 19:59:12"
                },
                {
                    "Id": "455e0e3e-d769-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-05-19 19:46:07",
                    "Name": "answerliao",
                    "ProjectId": "1",
                    "UpdateTime": "2022-05-19 19:46:07"
                },
                {
                    "Id": "4d9b78ec-a9b2-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-03-22 15:33:01",
                    "Name": "axiangzheng",
                    "ProjectId": "1",
                    "UpdateTime": "2022-03-22 15:33:01"
                },
                {
                    "Id": "57ded737-a9b2-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-03-22 15:33:18",
                    "Name": "axiangzheng_1",
                    "ProjectId": "1",
                    "UpdateTime": "2022-03-24 16:19:16"
                },
                {
                    "Id": "4c2aa1d5-a9c5-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-03-22 17:48:59",
                    "Name": "chengg_test",
                    "ProjectId": "1",
                    "UpdateTime": "2022-03-22 17:48:59"
                },
                {
                    "Id": "4eae14e2-9602-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-02-25 14:15:19",
                    "Name": "coolin",
                    "ProjectId": "1",
                    "UpdateTime": "2022-02-25 14:15:19"
                },
                {
                    "Id": "ef0a14f1-e88c-11ec-8909-bc97e105ba60",
                    "CreateTime": "2022-06-10 15:14:14",
                    "Name": "daorutest",
                    "ProjectId": "1",
                    "UpdateTime": "2022-06-10 15:14:14"
                }
            ]
        }
    }
}
```


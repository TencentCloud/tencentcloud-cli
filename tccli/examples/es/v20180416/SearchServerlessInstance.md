**Example 1: SearchServerlessInstance-SQLGroupBY**

SearchServerlessInstance-SQLGroupBY

Input: 

```
tccli es SearchServerlessInstance --cli-unfold-argument  \
    --Query select host.ip,count(*) from \"zxw-cvm-01-lgn9an13\" group by host.ip \
    --QueryType 1 \
    --TimeStampFrom 2023-03-08T11:06:07.000Z \
    --TimeStampTo 2023-09-25T11:06:07.000Z \
    --ServerlessId index-1u6t01yf \
    --Preference ddd \
    --Username elastic \
    --Password W*Fk=L?!62K38J_g51a7
```

Output: 
```
{
    "Response": {
        "Columns": [
            {
                "Name": "host.ip",
                "Type": "text"
            },
            {
                "Name": "count(*)",
                "Type": "long"
            }
        ],
        "Count": 0,
        "Cursor": "y+ezAwFaAWMBE3p4dy1jdm0tMDEtbGduOWFuMTOHAQEBCWNvbXBvc2l0ZQdncm91cGJ5AAD/AQAIYTVlOTQwN2EBD2hvc3QuaXAua2V5d29yZAAAAQAAZAEKAQhhNWU5NDA3YQAXZmU4MDo6NTA1NDpmZjpmZTc4Ojg4NWIAAgEAAAAAAP////8PAAAAAAAAAAAAAAAAAVoDAAICAAAAAAAAAAAKAP////8PAgFrCGE1ZTk0MDdhAAABawhhNWU5NDA3YQEAAQMA",
        "RequestId": "ae052ed0-0335-4f07-a5df-e2364f82de10",
        "Results": null,
        "Rows": [
            "[null,21297]",
            "[\"172.16.43.21\",4272328]",
            "[\"fe80::5054:ff:fe78:885b\",4272328]"
        ],
        "SearchAfterKeyFirst": null,
        "SearchAfterKeyLast": null
    }
}
```


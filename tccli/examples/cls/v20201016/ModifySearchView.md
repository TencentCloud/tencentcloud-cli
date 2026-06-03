**Example 1: 修改查询视图**



Input: 

```
tccli cls ModifySearchView --cli-unfold-argument  \
    --ViewId b*******_test_00001-view \
    --ViewName b*******_test_00001-update \
    --ViewType log \
    --Description b*******-tag-key-value test
```

Output: 
```
{
    "Response": {
        "RequestId": "6c5a7a89-42d9-41df-8093-b8237a061dbd"
    }
}
```


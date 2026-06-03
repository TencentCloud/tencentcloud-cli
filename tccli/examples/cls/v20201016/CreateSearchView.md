**Example 1: 创建查询视图**



Input: 

```
tccli cls CreateSearchView --cli-unfold-argument  \
    --LogsetId b*******-diy-1254139626 \
    --LogsetRegion ap-************** \
    --ViewName b*******_test_00001 \
    --ViewType log \
    --Topics.0.Region ap-guang********* \
    --Topics.0.LogsetId 1dbef1b5-2559-45fd-b41f-272ebd5a4535 \
    --Topics.0.TopicId b*******-diy-1254139626 \
    --ViewIdPrefix b*******_test_00001 \
    --Description b*******-tag-key-value test
```

Output: 
```
{
    "Response": {
        "ViewId": "b*******_test_00001-view",
        "RequestId": "550f786a-3943-43f0-a88e-1c3222bee72d"
    }
}
```


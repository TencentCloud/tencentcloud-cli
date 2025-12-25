**Example 1: 可用区为广州七区或广州八区的资源，按标签分组计数**



Input: 

```
tccli cloudrc GetResourceCount --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ConditionRule.ComplexArray.0.Type simple \
    --ConditionRule.ComplexArray.0.SimpleKey ZoneId \
    --ConditionRule.ComplexArray.0.SimpleOption equals \
    --ConditionRule.ComplexArray.0.SimpleValue 100008 100007 \
    --ConditionRule.ComplexOption or \
    --ConditionRule.Type complex \
    --Type tag
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "TagKey": "部门",
                "TagValue": "开发部",
                "Count": 25
            },
            {
                "TagKey": "部门",
                "TagValue": "测试部",
                "Count": 1
            },
            {
                "TagKey": "应用",
                "TagValue": "Web应用",
                "Count": 1
            }
        ],
        "RequestId": "2138d26f-fe46-4eb3-a0f6-fb3d86be3340"
    }
}
```

**Example 2: 所有资源按产品分组计数**



Input: 

```
tccli cloudrc GetResourceCount --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --Type product
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ProductCategory": "redis",
                "ProductKey": "cam::redis::instance",
                "Count": 472368
            },
            {
                "ProductCategory": "clb",
                "ProductKey": "cam::clb::clb",
                "Count": 8385
            },
            {
                "ProductCategory": "es",
                "ProductKey": "cam::es::instance",
                "Count": 5047
            },
            {
                "ProductCategory": "cvm",
                "ProductKey": "cam::cvm::instance",
                "Count": 4227
            },
            {
                "ProductCategory": "cbs",
                "ProductKey": "cam::cvm::volume",
                "Count": 4070
            },
            {
                "ProductCategory": "cdb",
                "ProductKey": "cam::cdb::instanceId",
                "Count": 986
            }
        ],
        "RequestId": "83a4bab1-9aaa-42ab-8e9f-222623b96124"
    }
}
```

**Example 3: 标记了部门=开发部、测试部的资源，按可用区分组计数**



Input: 

```
tccli cloudrc GetResourceCount --cli-unfold-argument  \
    --ViewId vw-6wyborpx \
    --ConditionRule.Type simple \
    --ConditionRule.SimpleKey tag:部门 \
    --ConditionRule.SimpleOption equals \
    --ConditionRule.SimpleValue 开发部 测试部 \
    --Type zone
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "RegionId": 1,
                "ZoneId": 100002,
                "Count": 40
            },
            {
                "RegionId": 1,
                "ZoneId": 0,
                "Count": 18
            },
            {
                "RegionId": 1,
                "ZoneId": 100001,
                "Count": 2
            },
            {
                "RegionId": 16,
                "ZoneId": 0,
                "Count": 2
            }
        ],
        "RequestId": "2138d26f-fe46-4eb3-a0f6-fb3d86be3340"
    }
}
```


**Example 1: 按 Label=stable 查询**

VersionId 与 Label 互斥；均省略时等价于 Label=stable。

Input: 

```
tccli ags DescribeRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```

**Example 2: 按 VersionId 精确查询**

指定 VersionId 时不返回 ResolvedLabel。

Input: 

```
tccli ags DescribeRegistryRecord --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "req-example"
    }
}
```


**Example 1: 删除空的非默认会话空间**

删除不再使用且不包含任何会话、事件或用户状态数据的普通会话空间。

Input: 

```
tccli ags DeleteSessionSpace --cli-unfold-argument  \
    --SpaceId space-22eed49f-e3ae-4b4a-8efa-4cd961bf4764
```

Output: 
```
{
    "Response": {
        "RequestId": "34b2cdc8-973c-4990-a1d9-614113e08f4f"
    }
}
```


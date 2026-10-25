**Example 1: 删除存储位置**

删除指定的存储位置

Input: 

```
tccli databuddy DeleteLocation --cli-unfold-argument  \
    --LocationName tmp_test_location \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Deleted": true
        },
        "RequestId": "063bb982-28b3-4e92-b683-94ed2da0d6f4"
    }
}
```


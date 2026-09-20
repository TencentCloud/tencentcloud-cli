**Example 1: 解绑被bundle绑定的资源**

解绑被bundle绑定的资源

Input: 

```
tccli wedata UnbindingResource --cli-unfold-argument  \
    --ProjectId 1464962169590902784 \
    --ResourceList.0.ResourceType TASK \
    --ResourceList.0.ResourceId 20250716170423856
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Code": "20250716170423856",
                "Message": "",
                "Success": true
            }
        ],
        "RequestId": "6b453935-44f9-47e8-bf9d-db6b0399a47f"
    }
}
```


**Example 1: 修改镜像的名称与描述**

修改镜像的名称与描述

Input: 

```
tccli lighthouse ModifyBlueprintAttribute --cli-unfold-argument  \
    --BlueprintId lhbp-1ynlfst1 \
    --BlueprintName new-blueprint \
    --Description new-blueprint
```

Output: 
```
{
    "Response": {
        "RequestId": "896682bb-fb47-4fce-94d9-9a4f2abbfaac"
    }
}
```


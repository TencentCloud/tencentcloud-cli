**Example 1: Creating video category**



Input: 

```
tccli vod CreateClass --cli-unfold-argument  \
    --ParentId -1 \
    --ClassName 'First-level Category 1' \
    --SubAppId 1
```

Output: 
```
{
    "Response": {
        "ClassId": 1,
        "RequestId": "38bac707-7f64-42fa-9369-cdddcc36550d"
    }
}
```


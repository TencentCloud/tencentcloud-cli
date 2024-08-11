**Example 1: 删除多个用户**



Input: 

```
tccli smh DeleteUser --cli-unfold-argument  \
    --LibraryId smh08gcw6500e6jl \
    --Filters.0.Key PhoneNumber \
    --Filters.0.Value +86-13800000000 \
    --Filters.1.Key Email \
    --Filters.1.Value admin@mail.foobar.com
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```


**Example 1: 验证Dspm资产登录验证码**



Input: 

```
tccli csip VerifyDspmAssetLoginCode --cli-unfold-argument  \
    --PersonId pid_zdazymzh \
    --AssetId cdb-c2thbt00 \
    --Code 00000
```

Output: 
```
{
    "Response": {
        "RequestId": "45ca21d4-f373-4274-9295-5380abc74bed",
        "Account": "dspm_bob",
        "Password": "DokJ6DDlgL48Mjbj+HeMLsGS4g1I+TtV2D9rA+xLmrCJG7rxSmHQx7VTdzrj8h1XtJl2hK+nlnJ0z1s/iT27Ao1MTcMrdiMwO3fCAtgm7jE5u//aix0nrwkEL84uvH1RaE+6ZL1zWs17ZPXhDtDOxLpAmYee/yzRpPOdrWAcgHhCzngUU61aeDwfS7eoC+z04b8aQumdbhrxkLZ5sa+hFdaLdWBP3yRWmaB8na9195jA2/vlo6fMrTwdU/oHX/hMYDcAElQbj4v+ERGT6SsBM3vfUsDLer3n6WR58Qu8wUUweQV46RbNTEpP/GJ3yNiwkPpLLUv1SSiox+KdwBgA0g==",
        "ValidateStart": "2025-01-01 12:00:00",
        "ValidateEnd": "2025-01-01 23:59:59"
    }
}
```


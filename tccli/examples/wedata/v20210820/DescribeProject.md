**Example 1: 样例**



Input: 

```
tccli wedata DescribeProject --cli-unfold-argument  \
    --ProjectId 1 \
    --DescribeAdminUsers True \
    --DescribeMemberCount True \
    --DescribeExecutors True \
    --DescribeClusters True
```

Output: 
```
{
    "Response": {
        "RequestId": "123"
    }
}
```

**Example 2: describe project with params**



Input: 

```
tccli wedata DescribeProject --cli-unfold-argument  \
    --ProjectId 978203585769070592
```

Output: 
```
{
    "Response": {
        "RequestId": "9ef8a942-efbe-4f77-8617-a9eb8875fea6"
    }
}
```

**Example 3: projectName transfer**



Input: 

```
tccli wedata DescribeProject --cli-unfold-argument  \
    --ProjectName unique_2rij3
```

Output: 
```
{
    "Response": {
        "RequestId": "949cd55d-e683-4698-a1cd-c142cf7b1e75"
    }
}
```


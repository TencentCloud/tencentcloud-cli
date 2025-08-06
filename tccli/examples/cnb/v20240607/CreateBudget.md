**Example 1: 创建预算单**



Input: 

```
tccli cnb CreateBudget --cli-unfold-argument  \
    --StorageGit 1 \
    --StorageObject 1 \
    --ComputeBuild 1 \
    --ComputeDevelop 1 \
    --BudgetName test-name
```

Output: 
```
{
    "Response": {
        "RequestId": "c4f1613e-7bb9-4fa2-bd75-a0a2c428bf39",
        "ResourceId": "700001520516-700001520516-1934518265978839040"
    }
}
```


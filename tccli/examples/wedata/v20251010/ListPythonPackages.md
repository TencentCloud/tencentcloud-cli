**Example 1: 成功**



Input: 

```
tccli wedata ListPythonPackages --cli-unfold-argument  \
    --WorkspaceId workspace_id_test \
    --KernelId 7e4c9d2b-6b8a-4f5e-9c3e-2a1f6b8d0c42 \
    --PageNumber 1 \
    --PageSize 10 \
    --Type None \
    --PackageName None
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Name": "numpy",
                    "Version": "1.24.3"
                },
                {
                    "Name": "pandas",
                    "Version": "2.0.3"
                },
                {
                    "Name": "matplotlib",
                    "Version": "3.7.2"
                },
                {
                    "Name": "scikit-learn",
                    "Version": "1.3.0"
                },
                {
                    "Name": "requests",
                    "Version": "2.31.0"
                },
                {
                    "Name": "flask",
                    "Version": "2.3.3"
                },
                {
                    "Name": "tensorflow",
                    "Version": "2.13.0"
                },
                {
                    "Name": "pytorch",
                    "Version": "2.0.1"
                },
                {
                    "Name": "jupyter",
                    "Version": "1.0.0"
                },
                {
                    "Name": "ipython",
                    "Version": "8.15.0"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 10,
            "TotalPageNumber": 1
        },
        "RequestId": "334be6b1-8600-44e9-baf0-4734d6e98b79"
    }
}
```


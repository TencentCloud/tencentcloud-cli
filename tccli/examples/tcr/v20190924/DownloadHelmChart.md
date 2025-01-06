**Example 1: 下载Helm Chart**



Input: 

```
tccli tcr DownloadHelmChart --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --NamespaceName chart \
    --ChartName mychart \
    --ChartVersion 0.1.0
```

Output: 
```
{
    "Response": {
        "Bucket": "tcr-dg284imq-1251707795",
        "ExpiredTime": 1735531292,
        "Path": "chart/mychart-0.1.0.tgz",
        "Region": "ap-guangzhou",
        "RequestId": "544d03c2-0eaf-422f-80f7-355d59ecec56",
        "StartTime": 1735527692,
        "TmpSecretId": "AKID3MccneCbtuvb4fJkrD9WhtldFVLLiN68dDuZsIz6UYZqgh6GSwYkkXlDM28lTEMn",
        "TmpSecretKey": "D+CIKDZ8tCG/WCDQ3ZW0P8jI2FTnAE4kDdfVJsXpx5k=",
        "TmpToken": "4oGxX3QwXFYLIyy01rbtYNzunag6Wp7ae7ac2c301dc22e35def4936b5f2adddbdlnEOlHBxFjaquqXiufCJ-rGUkrlGEzUpaXpEZEXpSN-Z9sVKhHzv4tTFRrCtBF36lC4II4ELiTyYemKJ5fyHGTSSe4hWnqOQaCKRTjRhd9LHr5e2SAhc3BiieW_Fmjr2IVWFAItWCZy4-uE-K5m56zrXM50Ye5Zp3d2fwqAKI5ZZYqsrV292gZj59wHX3KNOg_RHdrbLBSH3Qd5wsxEGDSAAWlfcNcsk5jbnJYhRQF29gyOgPSKoWCM17ZvsYsjdnN1E2Oi8Tkc8iud-K55C0rr1R4n5lCxD9AiJXfYFRDXXsRJHPuqzdWO5tmor8oBiWv_N-tcq_EdlPHcB_wYvxxOM1ezm73SX4QzE_mH7eQ"
    }
}
```


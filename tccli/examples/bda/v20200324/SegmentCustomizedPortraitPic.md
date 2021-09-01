**Example 1: 调用失败示例**



Input: 

```
tccli bda SegmentCustomizedPortraitPic --cli-unfold-argument  \
    --Url IamNotAUrl \
    --SegmentationOptions.Background False
```

Output: 
```
{
    "Response": {
        "RequestId": "46ed6f32-549f-4377-8116-2d55e4574528"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda SegmentCustomizedPortraitPic --cli-unfold-argument  \
    --Url test.jpg \
    --SegmentationOptions.Head True
```

Output: 
```
{
    "Response": {
        "PortraitImage": "iVBORw0KGgoAAAANSUhEUgAAAoAAAAHJCAYAAAAVcogaAAAgAElEQVR4AdThgZZlRRYYybpH3ELr/f/fNnm2D5FMVCcMXJVUdOvJzIXxGxUVlUNFZa3FoXKpXPqNd2aGo6LiqKiA4YXAoKLycqGicizkUpHfqRyuxVfJHzzEkVBxVFx7+K5ihIpriGOAiqPiGuKqOCquiqviqPgrFUfFVfHfonxS/pLKoXKttXin4h15T+VSOVQuFZW1Fmst1lqowHDsvThUVHBQUTmW37gqjoprZnhv8bNUDpWj4qhQOSoqZoaKimOKY2aomBkqKipUroqrAgcViL+j8vekEVj871J5R+VnVPwMlaOi4lBRgeHb64XGWou9N3tv1lqstVDZe6Oy92bvzVqLtRYqxyTHzDAzPM/D8zw8z0PF8zwcM0PFzFAxMxwzUHFUHCqHispVcVT8lYqr4qioqKj4aiE8IL9TOVQulb+TwzjkcFRcFcfMcFUcFd/14p2KQ+UrlWO/fkFFRWWthcpai6NCRUVF5auRT478TiqM38TMgB8wgR8c8cGK3wzw4lhrsffG...",
        "MaskImage": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAALCAHJAoABAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx...",
        "ImageRects": [
            {
                "Y": 1,
                "X": 2,
                "Height": 3,
                "Width": 4,
                "Label": "Head"
            }
        ],
        "RequestId": "07d71af0-d3af-4d36-8217-1e6836f38007"
    }
}
```


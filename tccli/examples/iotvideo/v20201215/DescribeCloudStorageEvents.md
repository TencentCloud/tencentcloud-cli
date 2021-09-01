**Example 1: 拉取云存事件列表**



Input: 

```
tccli iotvideo DescribeCloudStorageEvents --cli-unfold-argument  \
    --ProductId AQTV2839QJ \
    --DeviceName sp01_32820237_10
```

Output: 
```
{
    "Response": {
        "RequestId": "bd3ad0f6-5b9f-47cd-83db-223356926772",
        "Total": 13,
        "Events": [
            {
                "StartTime": 842084401,
                "EndTime": 842084401,
                "Thumbnail": "",
                "EventId": "id1_data"
            },
            {
                "StartTime": 842084401,
                "EndTime": 842084401,
                "Thumbnail": "",
                "EventId": "id1_data"
            },
            {
                "StartTime": 842084401,
                "EndTime": 842084401,
                "Thumbnail": "",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            },
            {
                "StartTime": 1614847697,
                "EndTime": 167000000,
                "Thumbnail": "face_dection.jpg",
                "EventId": "id1_data"
            }
        ],
        "Context": "DnF1ZXJ5VGhlbkZldGNoKAAAAAABxjxlFmlDUHBXME5XVE55eUdHMDUwZTV4WWcAAAAAAcaq9BZFeGQwTXM5X1RvNnFRMFNhRm1MNTlRAAAAAAHGqvYWRXhkME1zOV9UbzZxUTBTYUZtTDU5UQAAAAABxk0BFnN5Q1hWNUp0UjcyZkZma2licmF3SmcAAAAAAcaq9RZFeGQwTXM5X1RvNnFRMFNhRm1MNTlRAAAAAAHGhvUWTzl2c3FBNVdUWnFSWXh4d012MGlzdwAAAAABxjxmFmlDUHBXME5XVE55eUdHMDUwZTV4WWcAAAAAAcaG9xZPOXZzcUE1V1RacVJZeHh3TXYwaXN3AAAAAAHGVbkWTVBJSndzX0VReVNoU3JOb2pWUm40UQAAAAABxk0AFnN5Q1hWNUp0UjcyZkZma2licmF3SmcAAAAAAcaG-BZPOXZzcUE1V1RacVJZeHh3TXYwaXN3AAAAAAHGqvgWRXhkME1zOV9UbzZxUTBTYUZtTDU5UQAAAAABxkfDFjdNdGYtaTR5UTBPNmFFcHkyUmlUVHcAAAAAAcY88hZOVnkwbjNfNFRqV2YwSWk1LWczc2V3AAAAAAHGhvYWTzl2c3FBNVdUWnFSWXh4d012MGlzdwAAAAABxqr3FkV4ZDBNczlfVG82cVEwU2FGbUw1OVEAAAAAAcaG-RZPOXZzcUE1V1RacVJZeHh3TXYwaXN3AAAAAAHGR8IWN010Zi1pNHlRME82YUVweTJSaVRUdwAAAAABxquSFnJKTjhzbk5mUmZxMVVCcVhpVUNTZFEAAAAAAcY8ZxZpQ1BwVzBOV1ROeXlHRzA1MGU1eFlnAAAAAAHGehEWTTRRa1JkRDhUek9qem1CSmNFbHhUZwAAAAABxqr5FkV4ZDBNczlfVG82cVEwU2FGbUw1OVEAAAAAAcZNBBZzeUNYVjVKdFI3MmZGZmtpYnJhd0pnAAAAAAHGVboWTVBJSndzX0VReVNoU3JOb2pWUm40UQAAAAABxnoQFk00UWtSZEQ4VHpPanptQkpjRWx4VGcAAAAAAcarkxZySk44c25OZlJmcTFVQnFYaVVDU2RRAAAAAAHGTQIWc3lDWFY1SnRSNzJmRmZraWJyYXdKZwAAAAABxpZ4Fno4eVNTTDlLUVUyblVfMFFFcnhramcAAAAAAcY88xZOVnkwbjNfNFRqV2YwSWk1LWczc2V3AAAAAAHGTQMWc3lDWFY1SnRSNzJmRmZraWJyYXdKZwAAAAABxkfEFjdNdGYtaTR5UTBPNmFFcHkyUmlUVHcAAAAAAcarlBZySk44c25OZlJmcTFVQnFYaVVDU2RRAAAAAAHGqvoWRXhkME1zOV9UbzZxUTBTYUZtTDU5UQAAAAABxpZ6Fno4eVNTTDlLUVUyblVfMFFFcnhramcAAAAAAcZHxRY3TXRmLWk0eVEwTzZhRXB5MlJpVFR3AAAAAAHGVbsWTVBJSndzX0VReVNoU3JOb2pWUm40UQAAAAABxpZ5Fno4eVNTTDlLUVUyblVfMFFFcnhramcAAAAAAcY8aBZpQ1BwVzBOV1ROeXlHRzA1MGU1eFlnAAAAAAHGqvsWRXhkME1zOV9UbzZxUTBTYUZtTDU5UQAAAAABxpZ7Fno4eVNTTDlLUVUyblVfMFFFcnhramc=",
        "Listover": false,
        "VideoURL": "http://test.iotvideo.tencentcs.com/timeshift/live/test.m3u8"
    }
}
```


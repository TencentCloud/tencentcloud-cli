**To describe an unspecified public image**

This example describes an unspecified public image of Tencent Cloud.

Command::

    tccli cvm DescribeImages --Filter '[{"Name":"image-type","Values":["PUBLIC_IMAGE"]}]' --Limit 1

Output::

    {
        "Response": {
            "ImageSet": [
                {
                    "ImageId": "img-dkwyg6sr",
                    "OsName": "CentOS 7.3 64位",
                    "ImageSize": 50,
                    "ImageType": "PUBLIC_IMAGE",
                    "CreatedTime": null,
                    "ImageState": "NORMAL",
                    "ImageSource": "OFFICIAL",
                    "ImageName": "CentOS 7.3 64位",
                    "ImageDescription": "CentOS 7.3 64位",
                    "ImageCreator": null
                }
            ],
            "TotalCount": 42,
            "RequestId": "f32a0acd-a962-4e76-8334-278bcab684c0"
        }
    }

**To describe a specified image**

This example describes a specified image of Tencent Cloud.

Command::

    tccli cvm DescribeImages --ImageIds '["img-ez7jwngr"]'

Output::

    {
        "Response": {
            "ImageSet": [
                {
                    "ImageId": "img-ez7jwngr",
                    "OsName": "Debian 8.2 32位",
                    "ImageSize": 50,
                    "ImageType": "PUBLIC_IMAGE",
                    "CreatedTime": null,
                    "ImageState": "NORMAL",
                    "ImageSource": "OFFICIAL",
                    "ImageName": "Debian 8.2 32位",
                    "ImageDescription": "Debian 8.2 32位",
                    "ImageCreator": null
                }
            ],
            "TotalCount": 1,
            "RequestId": "56318750-dfbe-4f67-ba86-0df73cc00929"
        }
    }

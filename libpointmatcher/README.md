## Build image

To pre-build the image of the library you must use the following command to 
pull. The dockerfile script pulls directly from the GitHub repository using this branch :

`agagnon/project/server-eval`

In the future, this will be changed to an official image.
The download could take some time.

```bash
$ docker build . -t libpointmatcher
```

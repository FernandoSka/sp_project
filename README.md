# sp_project
test for spsolutions
- Get:
```
curl -XGET 'http://127.0.0.1:8000/api/sps/helloworld/v1'
```
response:
```
{
    "code": "yo get something"
}
```
- Post:
```
curl -XPOST 'http://127.0.0.1:8000/api/sps/helloworld/v1'
```
response:
```
{
    "code": "yo post something"
}
```
- Put:
```
curl -XPUT 'http://127.0.0.1:8000/api/sps/helloworld/v1'
```
response:
```
{
    "code": "yo put something"
}
```
- Delete:
```
curl -XDELETE 'http://127.0.0.1:8000/api/sps/helloworld/v1'
```
response:
```
{
    "code": "yo delete something"
}
```

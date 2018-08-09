# Basic Git commands

### Clone a git repository to your local machine
```
git clone <"paste the url of the repository">
```

### Set a remote repository you cloned or forked
```
> set remote
> set <"url of the repository">
```

### Initialize the repository
```
> git init
```

### Edit or create files in the repository using Unix/Linux text editors like vim

### Check status to see files currently not tracked
```
> git status
```

### Add the newly edited or created files to the tracking queue
```
> git add <"file name">
```

### Check status again to be sure
```
> git status
```


### Commit the added files
```
> git commit -m "Type a message to indicate you activity"
```

### Chech the status again
```
> git status
```

### Now push your committed files ti your online repository
```
> git push -u origin master
```

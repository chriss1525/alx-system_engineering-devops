# 0x17-web_stack_debugging_3

Let's automates the process of fixing an Apache 500 error. 

This solution uses the exec resource type to execute a command that corrects the issue in the wp-settings.php file.

- Step 1: Identifying the Issue


Use strace to trace Apache's execution and find the root cause of the 500 error.


Identify the issue in the wp-settings.php file causing the error.


- Step 2: Manual Resolution


Manually correct the issue in the wp-settings.php file.


Ensure that the 500 error is resolved by testing.


- Step 3: Puppet Automation


Open the 0-fix_php_extensions.pp file.


This file contains Puppet code that automates the fix.


The exec resource type runs a command to modify the file.


- Step 4: Applying Puppet Manifest


Install Puppet on your system if not already done.

Run the Puppet manifest using the following command:

```sh
Copy code
puppet apply 0-fix_php_extensions.pp
```


Puppet will execute the command in the exec resource, fixing the issue.

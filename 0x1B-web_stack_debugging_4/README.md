# 0x1B-web_stack_debugging_4

For this task we were debugging the high number of failed requests after making 2000 requests, 100 at time on an nginx server.

## Issue Discovery


### Error Log Examination:


We began by examining the Nginx error log to identify any error messages or patterns. 

The command sudo tail -f /var/log/nginx/error.log was used to monitor the error log in real-time.

### Identifying the Error:


During load testing, we observed multiple occurrences of the "too many open files" error in the error log. 

This indicated that the server was exceeding its file descriptor limit.

### Checking Current ulimit:


To verify the current open file descriptor limit, we used the command ulimit -n. 

The output showed that the default limit was set to a value much lower than expected.

### solution Approach


We decided to address the issue by increasing the open file descriptor limit and optimizing Nginx's configuration using Puppet. 

Here's how we achieved that:

#### Puppet Manifest:


We created a Puppet manifest named 0-the_sky_is_the_limit_not.pp to automate the process of adjusting the ulimit and modifying Nginx's configuration.

#### Modifying ulimit:


In the manifest, we used the exec resource to modify the ulimit value in the Nginx default configuration file (/etc/default/nginx). 

The sudo sed command was used to replace the existing ULIMIT value with the desired value of 2000.

#### Applying Changes:


The exec resource was configured to execute the sudo sed command only if the current ULIMIT value in the configuration file matched the expected pattern. 

This ensured that the change was applied only if necessary.

#### Restarting Nginx:


After modifying the ulimit, the exec resource triggered the restart of the Nginx service using the command sudo service nginx restart.

Execution
To reproduce the solution, follow these steps:

- Clone this repository to your system.
- Review and modify the 0-the_sky_is_the_limit_not.pp file according to your environment and requirements.
- Execute the Puppet manifest using the command:

```Copy code
 puppet apply fix_nginx_ulimit.pp
```


#### Verification


After applying the Puppet manifest, monitor the Nginx error log and observe the server's behavior under load. 

Use the command ulimit -n to confirm that the open file descriptor limit has been adjusted. 

Ensure that the "too many open files" error no longer occurs during load testing.

# Postmortem: 0x19 System Engineering & DevOps Project Outage

## Overview

At approximately 06:00 WAT, an isolated Ubuntu 14.04 container running an Apache web server experienced an outage. GET requests resulted in `500 Internal Server Error` responses instead of the expected HTML file for a Holberton WordPress site.

## Incident Timeline

### Detection

The issue was first encountered around 19:20 PST by Brennan (BDB), who was assigned to resolve the problem upon the project release.

### Debugging Steps

1. **Process Check**
    - Used `ps aux` to check running processes.
    - Confirmed that two `apache2` processes (`root` and `www-data`) were running correctly.

2. **Configuration Review**
    - Examined the `sites-available` folder in `/etc/apache2/`.
    - Confirmed the web server was serving content from `/var/www/html/`.

3. **System Call Tracing**
    - Ran `strace` on the `root` Apache process while sending a GET request using `curl`. No useful information was obtained.
    - Repeated `strace` on the `www-data` process and found a `-1 ENOENT (No such file or directory)` error when attempting to access `/var/www/html/wp-includes/class-wp-locale.phpp`.

4. **File Inspection**
    - Investigated files in `/var/www/html/` using Vim.
    - Located the typo (`.phpp` instead of `.php`) in the `wp-settings.php` file (Line 137: `require_once( ABSPATH . WPINC . '/class-wp-locale.php' );`).

5. **Issue Resolution**
    - Corrected the typo by removing the trailing `p`.
    - Verified the fix by sending another GET request, which returned a 200 OK status.

6. **Automation**
    - Created a Puppet manifest to automate the fix for any future occurrences of the same issue.

## Root Cause

The root cause of the outage was a typo in the `wp-settings.php` file, where the WordPress application attempted to load a non-existent file `class-wp-locale.phpp` instead of `class-wp-locale.php`.

## Resolution

The typo was corrected, and the server resumed normal operations.

## Prevention

To prevent similar issues in the future, the following measures are recommended:

1. **Thorough Testing**
    - Ensure comprehensive testing of applications before deployment. This error would have been detected earlier with proper testing.

2. **Monitoring**
    - Implement uptime monitoring services (e.g., [UptimeRobot](https://uptimerobot.com/)) to receive immediate alerts for any website outages.

3. **Automation**
    - Utilize automation tools like Puppet to fix known issues automatically. The Puppet manifest [0-strace_is_your_friend.pp](https://github.com/bdbaraban/holberton-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp) was created to replace any `phpp` extensions with `php` in `wp-settings.php`.

## Conclusion

The outage was caused by a simple typographical error in the application code. The issue was promptly identified and resolved through systematic debugging and correction of the typo. Moving forward, enhanced testing and monitoring practices will help prevent similar outages.

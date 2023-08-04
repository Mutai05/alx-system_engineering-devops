Permissions:

1. chmod: This command is used to change the permissions of a file or directory in Linux. It allows you to add or remove permissions for the owner, group, and others (everyone else). The permissions are represented by three digits: user (owner) permissions, group permissions, and others permissions.

2. sudo: The "sudo" command stands for "Super User Do" and is used to execute a command with administrative or root privileges. It allows authorized users to perform tasks that require elevated permissions.

3. su: The "su" command stands for "Switch User" and is used to change the current user to another user or the root user. By default, if you type "su" without specifying a username, it will switch to the root user.

4. chown: The "chown" command is used to change the owner of a file or directory. It allows you to transfer ownership of a file to a different user.

5. chgrp: The "chgrp" command is used to change the group ownership of a file or directory. It allows you to transfer group ownership to a different group.

Linux file permissions:

- Each file and directory in Linux has three sets of permissions: read, write, and execute. These permissions are defined for three entities: owner, group, and others (everyone else).
- The permissions are represented as a single digit number: read (4), write (2), and execute (1). To represent multiple permissions, you add the numbers together.
- For example, if a file has read and write permissions for the owner, read-only for the group, and no permissions for others, the permission number would be 640 (4+2 for owner, 4 for group, and 0 for others).

Changing permissions, owner, and group of a file:

- To change permissions, you can use the "chmod" command, followed by the permission number and the file/directory name.
- To change the owner, use the "chown" command, followed by the new owner's username and the file/directory name.
- To change the group, use the "chgrp" command, followed by the new group name and the file/directory name.

Why can't a normal user chown a file:

- Regular users are not allowed to change the ownership of files to prevent unauthorized access to sensitive data or system files. Only the root user (superuser) has the privilege to change ownership, ensuring the system's security and integrity.

Running a command with root privileges:

- To run a command with root privileges, use the "sudo" command before the actual command. For example: "sudo apt-get update" will execute the "apt-get update" command with root privileges.

Changing user ID or becoming superuser:

- To change the user ID or become the superuser (root), use the "su" command. To become the root user, simply type "su" and enter the root password when prompted.

Other Man Pages:

- Creating a user: You can create a new user using the "useradd" or "adduser" command. For more details, check the "man useradd" or "man adduser" pages.

- Creating a group: To create a group, use the "groupadd" command. Refer to the "man groupadd" page for additional information.

- Printing real and effective user and group IDs: The "id" command can be used to display the real and effective user and group IDs of the current user.

- Printing the groups a user is in: To list the groups a user belongs to, use the "groups" command followed by the username.

- Printing the effective user ID: You can use the "id -u" command to print the effective user ID of the current user.

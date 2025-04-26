import subprocess

def execute(command, device=None, use_shell=False):
    """
    Executes a simple ADB command and returns the result.

    This method is used for general ADB commands such as `adb devices`, `adb install`, etc.

    Args:
        command (str): The ADB command to execute.
        device (str, optional): The device ID. If specified, the command will be executed on this device.
        use_shell (bool, optional): Whether to execute the command in a shell on the device. Defaults to False.

    Returns:
        str: The output of the ADB command if successful, or "Unknown" if the command fails.

    Raises:
        subprocess.CalledProcessError: If the ADB command fails.
    """
    try:
        # Build the ADB command
        adb_command = ["adb"]

        if device:
            adb_command += ["-s", device]

        adb_command += command.split()

        # Execute the command
        result = subprocess.check_output(adb_command, stderr=subprocess.STDOUT, shell=use_shell)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return "Unknown"

def execute_shell(command, device=None):
    """
    Executes a shell command on the Android device and returns the result.

    This method is used for more complex shell commands that may require multiple commands 
    or shell-specific syntax (such as loops, conditionals, pipes, etc).

    Args:
        command (str): The shell command to execute on the device.
        device (str, optional): The device ID. If specified, the command will be executed on this device.

    Returns:
        str: The output of the shell command if successful, or an error message if the command fails.

    Raises:
        subprocess.CalledProcessError: If the shell command fails.
    """
    # Build the ADB shell command
    adb_command = ["adb"]

    if device:
        adb_command += ["-s", device]
        
    adb_command += ["shell", command]

    try:
        # Execute the command
        result = subprocess.check_output(adb_command, stderr=subprocess.STDOUT, shell=False)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return "Unknown"

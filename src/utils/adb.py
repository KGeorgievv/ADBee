import subprocess

def execute(command, device = None, use_shell=False):
    """
    Executes an ADB (Android Debug Bridge) command and returns the result.

    Args:
        command (str): The ADB command to execute.
        device (str, optional): The ID of the target device. If specified, the command will be executed on this device.
        use_shell (bool, optional): Whether to execute the command using the shell. Defaults to False.

    Returns:
        str: The output of the ADB command if successful, or an error message if the command fails.

    Raises:
        subprocess.CalledProcessError: If the ADB command fails, an error message is captured and returned.
    """

    try:
        if device:
            command = f"-s {device} {command}"

        result = subprocess.check_output(["adb"] + command.split(), stderr=subprocess.STDOUT, shell=use_shell)
        return result.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return "Unknown"

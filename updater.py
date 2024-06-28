import subprocess
import urllib.request

def update_client_version(version):
  """
  Checks if the local version (stored in version.txt) matches the provided version.

  Args:
      version: The version string to compare with the local version.

  Returns:
      True if the versions differ, False otherwise.
  """
  with open("version.txt", "r") as vnum:
    if vnum.read().strip() != version.strip():  # Added strip() for cleaner comparison
      return True
    else:
      return False

def main():
  """
  Checks for updates and performs a git pull if necessary.

  Prints a message indicating the update status.
  """
  try:
    version = urllib.request.urlopen("https://raw.githubusercontent.com/4w4k3/BeeLogger/master/version.txt").read().decode("utf-8")  # Added decode for proper string handling
  except urllib.error.URLError as e:
    print(f"Error: Failed to check for updates. {e}")
    return

  if update_client_version(version):
    subprocess.call(["git", "pull", "origin", "master"])
    print("[*] Updated to latest version: v{}..".format(version))
  else:
    print("[*] You are already up to date with git origin master.")

if __name__ == '__main__':
  print("[*] Checking version information..")
  print(main())

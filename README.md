Megalocyathus
-------------
![Enteroctopus Megalocyathus](mega.jpeg?raw=true)

A simple server for rapid internal deployment of simple POC apps.

It will:
* Receive a git push from a project containing a configuration file.
* Run a set of commands specified in the configuration to get the project up-and-running.
* Automatically supply ports, and make the project available at some configured names.

# Configuration

The configuration file is JSON, and consists of a few sections as possible:

```json
{
  "services": ["shortlink_name", ...]
  "dependencies": ["python", "!wget some_other_dep"],
  "exec": ["./start.sh --port={service_machine_name}", ...],
}
```

## Services

Services will be replaced with port numbers in "exec" commands.

You will also be able to reach your application at megalocyathus/service_machine_name

## Dependencies

The dependencies section lists what package manager applications must be installed.
Any dependencies not managed by the package manager should be installed with

## Exec

Will be sent to bash, in order, each time the git repository updates locally.


Internal Configuration
----------------------

Megalocyathus requires a few config details of its own:

```json
{
  "install_command": "pacman -Syu && pacman -S " // Dependency names will be appended to this.
}
```

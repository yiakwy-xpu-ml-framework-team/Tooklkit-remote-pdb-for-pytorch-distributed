===
Introduction
===

Remote PDB used in pytorch distributed environment (Megatron-LM).

* Free software : MIT license

installation
============

Prerequsite:

::
    sudo apt-get update && apt-get install socat rlwrap

See examples in [CUDA12 dockerfile](https://github.com/yiakwy-xpu-ml-framework-team/dockerhub/blob/main/cuda/Dockerfile.megatron-lm.ubuntu-22.04)

And simply include the project into dependencies. Pipy hosting is pending.

Usage
======

.. code:: python
    from remote_pdb import set_trace

The console will print the command for you to connect any Pytorch Rank. Just copy and execute it.
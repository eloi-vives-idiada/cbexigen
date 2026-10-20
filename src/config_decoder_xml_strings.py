# SPDX-License-Identifier: Apache-2.0
"""Focused ISO 15118-20 CommonMessages XML-string decoder configuration.

This derives the shared defaults from ``config.py`` but generates only the
CommonMessages datatype and decoder files. XML output is enabled, so generated
public decoder APIs include ``char *xmlOut, size_t xmlOut_size``.

The static EXI support files are intentionally not regenerated here. Generate
the default configuration once, or provide those headers from an existing
cbV2G build, when compiling this focused output.
"""

from config import *  # noqa: F401,F403 - derive generator defaults intentionally

# Keep focused artifacts separate from the standard full-codec output.
output_dir = 'output/xml-string-common'
log_dir = 'output/log/xml-string-common'

# Enable XML output for generated decoder functions.
generate_xml_output = 1

# Fragment decoders are outside this focused datatype/decoder configuration.
generate_fragments = 0

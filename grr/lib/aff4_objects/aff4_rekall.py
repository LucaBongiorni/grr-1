#!/usr/bin/env python
"""AFF4 objects for managing Rekall responses."""

from grr.client.components.rekall_support import rekall_types as rdf_rekall_types

from grr.lib.aff4_objects import sequential_collection


class RekallResponseCollection(sequential_collection.GeneralIndexedCollection):
  """A collection of Rekall results."""
  _rdf_type = rdf_rekall_types.RekallResponse

  renderer = "GRRRekallRenderer"

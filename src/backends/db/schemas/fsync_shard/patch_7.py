# Copyright 2008-2015 Canonical
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# For further info, check  http://launchpad.net/filesync-server

"""Set a lower threashold for autovacuum in big tables."""

SQL = [
    """
    ALTER TABLE ContentBlob SET (autovacuum_vacuum_scale_factor = 0.02);
    """,
    """
    ALTER TABLE UploadJob SET (autovacuum_vacuum_scale_factor = 0.02);
    """,
    """
    ALTER TABLE Object SET (autovacuum_vacuum_scale_factor = 0.02);
    """,
]


def apply(store):
    """Apply the patch."""
    for sql in SQL:
        store.execute(sql)

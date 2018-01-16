# -*- coding: utf-8 -*-
# Copyright 2017 Leo Moll and Dominik Schlösser
#

# -- Imports ------------------------------------------------
import sys
import xbmcgui
import xbmcplugin

import resources.lib.mvutils as mvutils

from resources.lib.channel import Channel

# -- Classes ------------------------------------------------
class ChannelUI( Channel ):
	def __init__( self, handle, sortmethods = None, nextdir = 'initial' ):
		self.nextdir		= nextdir
		self.handle			= handle
		self.sortmethods	= sortmethods if sortmethods is not None else [ xbmcplugin.SORT_METHOD_TITLE ]
		self.count			= 0

	def Begin( self ):
		for method in self.sortmethods:
			xbmcplugin.addSortMethod( self.handle, method )

	def Add( self, altname = None ):
		resultingname = self.channel if self.count == 0 else '%s (%d)' % ( self.channel, self.count, )
		li = xbmcgui.ListItem( label = resultingname if altname is None else altname )
		xbmcplugin.addDirectoryItem(
			handle	= self.handle,
			url		= mvutils.build_url( {
				'mode': self.nextdir,
				'channel': self.id
			} ),
			listitem = li,
			isFolder = True
		)

	def End( self ):
		xbmcplugin.endOfDirectory( self.handle )

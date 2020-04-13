// Copyright (C) 2011-2020 ycmd contributors
//
// This file is part of ycmd.
//
// ycmd is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// ycmd is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with ycmd.  If not, see <http://www.gnu.org/licenses/>.


#ifndef FILESUTILS_H_KEPMRPBH
#define FILESUTILS_H_KEPMRPBH

#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

namespace YouCompleteMe {


// Reads the entire contents of the specified file. If the file does not exist,
// an exception is thrown.
std::string ReadUtf8File( const fs::path &filepath );


// Normalizes a path by making it absolute relative to |base|, resolving
// symbolic links, removing '.' and '..' in the path, and converting slashes
// into backslashes on Windows. Contrarily to boost::filesystem::canonical, this
// works even if the file doesn't exist.
YCM_EXPORT fs::path NormalizePath( const fs::path &filepath,
                                   const fs::path &base = fs::current_path() );


} // namespace YouCompleteMe

#endif

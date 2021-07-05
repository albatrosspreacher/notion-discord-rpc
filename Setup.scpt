set windowTitles to {}
set visibleProcesses to {}
set visibleProcessesWithWindows to {}

tell application "System Events"
	set visibleProcesses to name of (every process whose visible is true)
	repeat with processName in visibleProcesses
		if (count windows of process processName) is not 0 then
			set end of visibleProcessesWithWindows to processName
			set end of windowTitles to (name of every window of process processName)
			if processName begins with {"Notion"} then
				return windowTitles as text
			end if
		end if
	end repeat
end tell
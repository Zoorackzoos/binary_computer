import re


def clean_operand(op):
    """Remove AT&T syntax symbols."""
    return op.replace("$", "").strip()


def translate(instruction):
    """
    Convert an x86 AT&T instruction into a formula representation.
    """

    # remove address / opcode bytes if present
    instruction = instruction.split("\t")[-1].strip()

    parts = instruction.split(None, 1)
    opcode = parts[0]

    operands = []
    if len(parts) > 1:
        operands = [o.strip() for o in parts[1].split(",")]

    # AT&T syntax: source, destination
    src = operands[0] if len(operands) >= 1 else None
    dst = operands[1] if len(operands) >= 2 else None

    if src: src = clean_operand(src)
    if dst: dst = clean_operand(dst)

    if opcode.startswith("mov"):
        return f"{dst} = {src}"

    if opcode.startswith("add"):
        return f"{dst} = {dst} + {src}"

    if opcode.startswith("sub"):
        return f"{dst} = {dst} - {src}"

    if opcode.startswith("imul"):
        return f"{dst} = {dst} * {src}"

    if opcode.startswith("and"):
        return f"{dst} = {dst} & {src}"

    if opcode.startswith("or"):
        return f"{dst} = {dst} | {src}"

    if opcode.startswith("xor"):
        return f"{dst} = {dst} ^ {src}"

    if opcode.startswith("shl") or opcode.startswith("sal"):
        return f"{dst} = {dst} << {src}"

    if opcode.startswith("shr"):
        return f"{dst} = {dst} >> {src}"

    if opcode.startswith("lea"):
        return f"{dst} = address({src})"

    return f"Unsupported instruction: {instruction}"


# Example usage
lines = [
    "48 83 ec 08           sub    $0x8,%rsp",
    "mov $5,%rax",
    "add %rbx,%rax",
    "imul %rcx,%rax"
]

for l in lines:
    print(l)
    print(" -> ", translate(l))
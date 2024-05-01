import { Controller, Get } from '@nestjs/common';
@Controller()
export class RacineController {
  constructor(
  ) {}

  @Get()
  getPrez(): string {
    return `
    <a href="/queue/">/queue/</a><br>
    `;
  }

}
